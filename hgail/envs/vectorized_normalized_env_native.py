import numpy as np
from rllab.envs import normalized_env_native
from rllab.core import serializable

class VectorizedNormalizedEnvNative(normalized_env_native.NormalizedEnvNative):

    def __init__(
            self,
            env,
            clip_std_multiple=np.inf,
            **kwargs):
        serializable.Serializable.quick_init(self, locals())
        self.clip_std_multiple = clip_std_multiple
        super(VectorizedNormalizedEnvNative, self).__init__(env, **kwargs)

    def _update_obs_estimate(self, obs):
        # assert (n_envs, obs_dim) shape, i.e., already flat
        assert len(obs.shape) == 2
        self._obs_mean = (1 - self._obs_alpha) * self._obs_mean + self._obs_alpha * np.mean(obs, axis=0)
        self._obs_var = (1 - self._obs_alpha) * self._obs_var + self._obs_alpha * np.mean(np.square(obs - self._obs_mean), axis=0)

    def _apply_normalize_obs(self, obs):
        self._update_obs_estimate(obs)
        std = np.sqrt(self._obs_var) + 1e-8
        return np.clip(
            obs - self._obs_mean,
            -std * self.clip_std_multiple,
            std * self.clip_std_multiple
        ) / std

    @property
    def vectorized(self):
        return True

    def vec_env_executor(self, n_envs, max_path_length):
        self.num_envs = n_envs
        return self

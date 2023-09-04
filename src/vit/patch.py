from torch import nn


class Patch(nn.Module):
    def __init__(self, patch_size):
        super().__init__()
        self.patch_size = patch_size

    def forward(self, x):
        """Reshapa x into patches

        Args:
            x (Tensor, shape=(B, C, H, W)): Input tensor.

        Returns:
            Tensor, shape=(B, N, C * patch_size * patch_size): Output tensor.
        """
        B, C, H, W = x.shape
        x = x.reshape(
            B,
            C,
            H // self.patch_size,
            self.patch_size,
            W // self.patch_size,
            self.patch_size,
        )
        x = x.permute(0, 2, 4, 1, 3, 5)
        x = x.reshape(B, -1, C * self.patch_size * self.patch_size)
        return x

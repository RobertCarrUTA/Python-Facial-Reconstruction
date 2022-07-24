import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image

# Load raw images
data_dir = "/home/student/Desktop/ExtraCredit/ATTfaces/faces/"
file_names = os.listdir(data_dir)
images = [np.asarray(Image.open(data_dir + file_names[i])) for i in range(len(file_names))]
images = np.array(images)

# Visualize some of the faces
fig = plt.figure(figsize=(8, 8))
grid = ImageGrid(fig, 111, nrows_ncols=(8, 8), axes_pad=0)

for ax, im in zip(grid, images[:64]):
    ax.imshow(im)
    ax.axis('off')

# Calculate the mean face
face_mean = np.mean(images, 0)

num_images = len(images)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(face_mean)

num_images, height, width = images.shape

def compute_pca(data, data_mean):
    # 1. Subtract the mean image from all images
    data = data.astype('float64')  # Need to make the types match, so make data float64
    data -= data_mean
   
    # 2. Vectorize the images to a 400 x 10304 matrix -- use reshape
    data = np.reshape(data, (400, 10304))
   
    # 3. Create the covariance matrix
    covariance = (1/(num_images - 1)) * (data @ data.T)
   
    # 4. Compute the eigendecomposition -- try np.linalg.eig
    eigenvalues, eigenvectors = np.linalg.eig(covariance)
   
    # 5. Calculate the eigenfaces: U = XV
    eigenfaces = eigenvectors.T @ data
   
    # 6. Normalize the eigenfaces to that they are unit vectors
    eigenfaces = eigenfaces/np.linalg.norm(eigenfaces, axis = 1)[:, np.newaxis] # U/magnitude of U
   
    # 7. Compute the weights by projected the centered data(u) onto the eigenfaces(v)
    weights = data @ eigenfaces.T
   
    # 8. Return the normalized eigenfaces and weights
    return eigenfaces, weights

# Compute PCA and visualize
eigenfaces, weights = compute_pca(images, face_mean)

# Visualize some eigenfaces
fig = plt.figure(figsize=(8, 8))
grid = ImageGrid(fig, 111, nrows_ncols=(4, 4), axes_pad=0)

for ax, im in zip(grid, eigenfaces[:16]):
    ax.imshow(im.reshape(height, width))
    ax.axis('off')

def reconstruct(weights, eigenfaces, X_mean, img_size, img_idx, n_comps):
  
    w_matmul_u = (weights[img_idx, :n_comps] @ eigenfaces[:n_comps, :])
    
    recovered_img = X_mean + w_matmul_u
    recovered_img = recovered_img.reshape(img_size)
    
    return recovered_img

img_idx = 50
n_comps = 400

recovered_img = reconstruct(weights, eigenfaces, face_mean.reshape(-1), [height, width], img_idx, n_comps)

# Visualize original and reconstructed
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(images[img_idx])
ax2.imshow(recovered_img)
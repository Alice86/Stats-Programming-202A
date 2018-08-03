import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


def s(x, y, sigma=1.0):
    return np.exp(-1/(2 * sigma**2) * np.sum((x - y)**2))


def create_S(X, s, eps=1.0e-50):
    n = X.shape[0]
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            sij = s(X[i,:], X[j,:])
            if sij >= eps:  
                S[i,j] = sij
                S[j,i] = sij
    ################################
    # TODO (1) implement
    # (1) note, s(x,y) is a function
    # (2) note, set S[i,j] = 0 if s(x,y) < eps
    ################################

    return S


def create_L(X, s):
    n = X.shape[0]
    S = create_S(X, s)
    D_prime = np.zeros((n, n))
    for i in range(n):
        d = np.sum(S[i,:])
        D_prime[i,i] = 1.0/(d ** 0.5)

    ################################
    # TODO (2) implement
    ################################

    L = np.dot(np.dot(D_prime, S), D_prime)
    return L


def create_Y(X, s, num_eigs=2):
    n = X.shape[0]
    L = create_L(X, s)
    _, Z1 = np.linalg.eig(L)
    Z = Z1[:, :num_eigs]
    Y = np.zeros((n, num_eigs))
    for i in range(n):
        z = Z[i, :]
        Y[i, ] = (z / (np.sum(z ** 2) ** 0.5))
    return Y


def k_means(X, k=2, tol=1e-6, max_iter=300, break_limit=5, num_restarts=10):
    n, p = X.shape
    performances = np.zeros(num_restarts)
    cluster_array = np.zeros((n, num_restarts))
    for t in range(num_restarts):
        centroids = np.zeros((k, p))
        shuffle_X = shuffle(X)
        for i in range(k):
            centroids[i] = shuffle_X[i]

        distances = np.zeros(max_iter)
        break_count = 1
        for iter in range(max_iter):
            cluster_membership = np.zeros(n)
            for i in range(n):
                dist_vec = np.zeros(k)
                for j in range(k):
                    dist_vec[j] = np.sum((X[i,:] - centroids[j,:])**2)
                cluster_membership[i] = np.argmin(dist_vec)
            cluster_membership = cluster_membership.astype(int)

            for i in range(k):
                centroids[i] = np.mean(X[cluster_membership == i, :], axis=0)

            ind_dist = np.zeros(n)
            for i in range(n):
                ind_dist[i] = np.sum((X[i,:] - centroids[cluster_membership[i],:])**2)
            distances[iter] = np.sum(ind_dist**2)

            distance_difference = np.sum((distances[iter] - distances[iter - 1])**2)
            break_count = break_count + 1 if distance_difference < tol else 1

            if break_count >= break_limit:
                break

        cluster_array[:,t] = cluster_membership
        performances[t] = distances[iter]

    best_iteration = np.argmin(performances)
    final_clusters = cluster_array[:, best_iteration]

    return final_clusters


def spectral_clustering(X, s, num_eigs=2, k=2):
    Y = create_Y(X, s, num_eigs)
    labels = k_means(Y, k)
    return Y, labels


def main():
    np.random.seed(1)

    def xy(eta, n):
        theta = np.random.uniform(0, 2 * np.pi, n)
        x = eta * np.cos(theta) + np.random.normal(0, 0.05, n)
        y = eta * np.sin(theta) + np.random.normal(0, 0.05, n)
        return x, y

    sigmas = [0.1, 0.2, 0.5, 1.0]
    num_eigs_list = [2**1, 2**2, 2**3, 2**4]

    x0, y0 = xy(0.1, 50)
    x1, y1 = xy(1.0, 200)
    x2, y2 = xy(2.0, 400)

    x = np.concatenate((x0, x1, x2), axis=0)
    y = np.concatenate((y0, y1, y2), axis=0)
    X = np.transpose(np.vstack((x, y)))

    create_s = lambda sigma: lambda x, y: s(x, y, sigma=sigma)

    for sigma in sigmas:
        fig, ax = plt.subplots()
        ax.matshow(create_S(X, create_s(sigma)), cmap=plt.cm.Reds)
        plt.title('S sigma = {}'.format(sigma))
        #plt.savefig('S sigma = {}.png'.format(sigma))
        # measures the similarity between i and j, bigger sigma, higher measure

    for sigma in sigmas:
        E1, Z1 = np.linalg.eig(create_L(X, create_s(sigma)))
        Z1 = Z1[:, E1.argsort()[::-1]]
        plt.figure()
        plt.plot(Z1[:, 1])
        plt.title('Eigenvector 1 sigma = {}'.format(sigma))
        plt.plot()
        plt.savefig('Eigenvector 1 sigma = {}.png'.format(sigma))

        plt.figure()
        plt.plot(Z1[:, 2])
        plt.title('Eigenvector 2 sigma = {}'.format(sigma))
        plt.plot()
        #plt.savefig('Eigenvector 2 sigma = {}.png'.format(sigma))
        # less distinct

    plt.figure()
    plt.scatter(x0, y0, c='r', marker='x')
    plt.scatter(x1, y1, c='b', marker='o')
    plt.scatter(x2, y2, c='g', marker='o')
    plt.title('True classes')
    #plt.savefig('True classes')
    plt.show()

    for num_eigs in num_eigs_list:
        for sigma in sigmas:
            Y, class_pred = spectral_clustering(X, create_s(sigma), k=3, num_eigs=num_eigs)

            plt.scatter(x[class_pred == 0], y[class_pred == 0], c='r', marker='x')
            plt.scatter(x[class_pred == 1], y[class_pred == 1], c='b', marker='o')
            plt.scatter(x[class_pred == 2], y[class_pred == 2], c='g', marker='o')
            plt.title('Spectral clustering results sigma = {}, num(eigs) = {}'.format(sigma, num_eigs))
            plt.plot()
            plt.savefig('Spectral clustering results sigma = {}, num(eigs) = {}.png'.format(sigma, num_eigs))

    kmeans_pred = k_means(X, k=3)

    plt.scatter(x[kmeans_pred == 0], y[kmeans_pred == 0], c='r', marker='x')
    plt.scatter(x[kmeans_pred == 1], y[kmeans_pred == 1], c='b', marker='o')
    plt.scatter(x[kmeans_pred == 2], y[kmeans_pred == 2], c='g', marker='o')
    plt.title('K-means clustering results')
    plt.plot()
    #plt.savefig('K-means clustering results.png')



if __name__ == '__main__':
    main()

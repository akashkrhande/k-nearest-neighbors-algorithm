# k-nearest-neighbors-algorithm
In years of my college into analytics I have built more than 80% of classification models and just 15-20% regression models. These ratios can be more or less generalized throughout the industry. The reason of a bias towards classification models is that most analytical problem involves making a decision. For instance will a customer attrite or not, should we target customer X for digital campaigns, whether customer has a high potential or not etc. These analysis are more insightful and directly links to an implementation roadmap. In this article, we will talk about another widely used classification technique called K-nearest neighbors (KNN) . Our focus will be primarily on how does the algorithm work and how does the input parameter effect the output/prediction.
Breaking it Down – Pseudo Code of KNN

We can implement a KNN model by following the below steps:

   1 Load the data
   2 Initialise the value of k
   3 For getting the predicted class, iterate from 1 to total number of training data points
        1 Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our        
          distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
        2 Sort the calculated distances in ascending order based on distance values
        3 Get top k rows from the sorted array
        4 Get the most frequent class of these rows
        Return the predicted class

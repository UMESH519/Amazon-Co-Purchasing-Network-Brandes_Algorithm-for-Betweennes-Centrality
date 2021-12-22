# Amazon-Co-Purchasing-Network-Brandes_Algorithm-for-Betweennes-Centrality
 
The project aims to discover if there is an association between the Sales Rank of a product and its betweenness centrality measure when the product is stored in a graph network.Though identifying popular and important products, they would be able to optimize their marketing budget improve the visibility of products that increases customer spending and thus improve profitability.  


## Glossary:  
Sales Rank: Measure of Popularity of the Product sold on Amazon.com. 

Betweenness Centrality : The betweenness centrality for each vertex is the number of these shortest paths that pass through the vertex scaled by the total no. of shortest path in the graph. 

Here Graph has been stores in a Adjacency Hash. Example: Graph({'A': {'C': 1}, 'C': {'D': 1, 'E': 1}, 'B': {'C': 1}, 'D': {'F': 1}, 'E': {'F': 1}, 'F': {'G': 1}, 'G': {}}). 
In the above example, Product C was purchased after Product A. Nothing was purchased after Product G


## Code:  

There are three .py files in this subfolder:
1) The first file *Algorithm.py* contains the code for the Brandes algorithm that calculates the Betweenness Centrality of a graph. 

2) The second python file is *main.py* which contains the code for the Graph Class. This is also the main execuatble file that will call all the functions to demonstrate the results of the project.

3) The third file is *Data_Cleaning.py*. This file contians code for parsing the original dataset and segregating it into three subset Datasets which are Low_rank_nodes, medium_rank_nodes and high_rank_nodes. Note that there is also a function called parse_rank which will extract the range of sales rank that the product in the dataset contains but the execution of this function is only needed if we want to change the criteria (range of sales rank) of dividing the original dataset. 
other functions in Data.Processing.py are parse_highrank_nodes, parse_mediumrank_nodes and parse_lowrank_nodes. These three functions work in a similar way. First these functions extract the rank from the line and compare it with the pre-defined intervals. If the rank lies in the preferred range, It further processes the "also_buy" key which contains the list of items which were also bought. This function is finally used to dump (to subset) a list of list where inner list contains all the edges from Product A to Product B, Product C , Product D etc. 

Example of the final output from the above three functions are :[[["B0002JBXG4", "B0009OAI4U"], ["B0002JBXG4", "B000C1Z4XU"]]]
Here the list signifies that Product "B0009OAI4U" and "B000C1Z4XU" were purchased after Product "B0002JBXG4".




## Data

The Dataset contains metadata of luxury beauty category and has been sourced from https://nijianmo.github.io/amazon/index.html.  Total Number of rows or products is 12308. As you can see below there are various fields present in the dataset. Each row is identified by the "asin" which is Id of the product. description of other keys is as follows:  The dataset is in dictionary format. To run the repository locally, Dataset can be downloaded from https://drive.google.com/file/d/1Sj28EPUb4IWVBMkVhFS4B8y4_KBKmyuA/view?usp=sharing

##### asin - ID of the product, e.g. 0000031852. 

title - name of the product. 

feature - bullet-point format features of the product. 

description - description of the product. 

price - price in US dollars (at time of crawl). 

imageURL - url of the product image. 

imageURL - url of the high resolution product image. 

related - related products (also bought, also viewed, bought together, buy after viewing). 

##### also_buy- purchased products. 

##### salesRank - sales rank information. 

brand - brand name. 

category - list of categories the product belongs to. 

tech1 - the first technical detail table of the product. 

tech2 - the second technical detail table of the product. 

similar - similar product table. 

Example of Raw Dataset:
                                                            ----------------------------------

{"category": [], "tech1": "", "description": [], "fit": "", "title": "DERMAdoctor Calm, Cool &amp; Corrected anti-redness tranquility cream - 1.7 Oz", "also_buy": ["B019EKOK6G", "B01EM44IEI", "B0186FLPUE", "B00RORUNQI", "B006TD38ZG", "B01EM4D85I", "B002VM7ILE", "B0000ZREXG", "B000OMPQ76", "B00VHJ13EA", "B00E1KLNW4", "B01EM45YNW", "B00RORUL6U", "B000FJU4HK", "B00VHJ0ZUS"], "tech2": "", "brand": "", "feature": [], "rank": "186,829 in Beauty &amp; Personal Care (", "also_view": ["B01ETQBD6U", "B019EKOK6G", "B01EM45YNW", "B0186FLPUE", "B07B8BN8H6", "B000FJU4HK", "B01EM44IEI", "B00RORUL6U", "B01FO1IT02", "B001FXOCT6", "B01EM45E4G", "B00RORUNQI", "B000Z61SSM", "B00VHJ13EA", "B002CML1XE", "B0000ZREXG", "B07B7HVPCB", "B071JS38YF", "B00ZPWR0N8", "B00E1KLNW4"], "details": {"\n    Product Dimensions: \n    ": "2.2 x 2.2 x 3.1 inches ; 1.76 ounces", "Shipping Weight:": "6.4 ounces (", "Domestic Shipping: ": "Item can be shipped within U.S.", "International Shipping: ": "This item is not eligible for international shipping.", "ASIN:": "B0000Y3NO6", "Item model number:": "174283"}, "main_cat": "Luxury Beauty", "similar_item": "", "date": "", "price": "$85.00", "asin": "B0000Y3NO6", "imageURL": ["https://images-na.ssl-images-amazon.com/images/I/41sTOlcsmjL._SX50_SY65_CR,0,0,50,65_.jpg", "https://images-na.ssl-images-amazon.com/images/I/81K-8p2lItL.SX50_SY65_CR,0,0,50,65_PKmb-play-button-overlay-thumb_.jpg"], "imageURLHighRes": ["https://images-na.ssl-images-amazon.com/images/I/41sTOlcsmjL.jpg", "https://images-na.ssl-images-amazon.com/images/I/81K-8p2lItL.jpg"]}
                                                           ----------------------------------

The fields "asin", "also_buy" and "rank" ( bolded ) were of interest and thus have been extracted in the Data Processing.py


## Results

Through the project, I was able to discover the association between Prododucts’s popularity and the betweenness centrality. As the popularity of the products improves the betweenness centrality measure also improves. The result folder contains the detailed final project report as well as the video presentation. 

## To run the code locally for the first time:
 After downloading the repository, There will only be a single file named original_data.json.gz in the data subfolder. Pls follow the below steps to run the code:
 the code:   
 
 1) Cline the directory to your specified folder
 2) Go to data subfolder and copy the Google drive link in you web browser to download the data. Stores the downloaded data in the data subdirectory.   
 3 ) Change the directory to the above folder and then to code subfolder.  
 4) First Run Data_Cleaning.py. This will create three files named high_rank_nodes, low_rank_nodes and medium_rank_nodes in data subfolder. A file named rank will also be generated but is only needed if we want to change the criteria of segregating the above files.  
 5) After this run main.py. Results will be generated in the Terminal.  
 6) If you want to create a new graph and calculate its Betweenenss Centrality, Create a new instance of the Graph class. and then Make an edgelist that contains a list of directed edges. After this Call add_edges method on graph instance and then call betweenness_centrality function with the graph instance as the function input. 



## Citation (For Dataset) 
Justifying recommendations using distantly-labeled reviews and fined-grained aspects. 

Jianmo Ni, Jiacheng Li, Julian McAuley. 

Empirical Methods in Natural Language Processing (EMNLP), 2019

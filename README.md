# project2
Product mission statement:
Product name: Explore Companion
Product Description: Explore Companion is a mobile application utilizing the Google map to develop product that can give the user a unique experience when they start a new journey to some place. No matter they’re a local explorer or an adventurous traveler, they can get their customizing trip plan and personalized experience, leaving every precious memory with them. Explore Companion will enable the users to create interactive and educational virtual tours for various purposes.
Target Audience: Travelers who are going to explore new places.
Key features: Personalized trip planner; weather & ticket booking together before trip; Google maps data integration; 3D environment creation; interactive navigation; export and sharing; 
MVP：
3D environment creation: Create the 3D models of the environment, which users want to see, including streets,buildings, and terrain, based on the imported data.
Recommendation of places:Use python to grab the data of  location and to recommend the places user interested in.

Using method:
main.py: use the pandas and google api to get the excel including information of "Address", "Longitude", "Latitude", "Name", "Rating" information of the place, the result can be seen in bars_info.xlsx.
app.py: run this code we can combine with the index.html under template folder utilizing the flask frame to get the website of the bars and also the rating.
3D model in the master branch: the 3D model from the google map can be opened in the times1.blend file. We can utilizing the 3D model to get the view of the place we want to go.
Attention: the api key needed when run the app.py and also the index.html
The newest version is bar1.html. It can achieve the function as: With more improvement, I realize the function that during my trip, the app can update the nearby bar or club when I walk by, and also update with the different color symbolizing the rating stars of  customers. The green represents highest recommendation, the red represents the lowest recommendation. The recommendation will update in few minutes and give notification.

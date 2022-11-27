from controller import get_user_input_topics, get_all_articles, get_random
from user import User
from os import system

if __name__ == "__main__":
	user = User()
	
	# Step 1: Get favorite topics from user input
	favorite_topics = get_user_input_topics()
	user.set_favorite_topics(favorite_topics)
	
	# Step 2: Create set of articles, based on favorite topics
	articles = set()
	for topic in user.get_favorite_topics():
		articles.update(get_all_articles(topic))
	
	# Step 3: Present articles to user
	while len(articles) > 0:
		
		# Select random article
		article = get_random(articles)

		# Ask the user if they want read article
		user_input = input("Do you want to read {} from topic {}? [yes/other] ".format(article.get_title(), article.get_topic()))

		if user_input == "yes":
			# Open article
			system("open {}".format(article.url))
			user.add_article_to_history(article)
			
			# Ask user if they want to read another article		
			user_input = input("Read more? {} articles remaining [yes/other] ".format(len(articles)))
			if user_input != "yes":
				break
	
		print("Looking for another article...")
	
	print("Total articles read: {}".format(len(user.get_articles_history)))
	print("end.")
		
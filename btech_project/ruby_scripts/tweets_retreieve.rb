require 'rubygems'
require 'restclient'
require 'crack'

MAX_NUMBER_OF_TWEETS = 3200
NUMBER_OF_TWEETS_PER_PAGE = 200

TARGET_USERNAME = 'bhogle'

DATA_DIRECTORY = "data-hold"

Dir.mkdir(DATA_DIRECTORY) unless File.exists?(DATA_DIRECTORY)

GET_USERINFO_URL = "http://api.twitter.com/1/users/show.xml?screen_name=#{TARGET_USERNAME}"
GET_STATUSES_URL = "http://api.twitter.com/1/statuses/user_timeline.xml?screen_name=#{TARGET_USERNAME}&trim_user=true&count=#{NUMBER_OF_TWEETS_PER_PAGE}&include_retweets=true&include_entities=true"

user_info = RestClient.get(GET_USERINFO_URL)

if user_info.code != 200
	puts "Failed to get a correct response from Twitter. Response code is: #{user_info.code}"

else
	File.open("#{DATA_DIRECTORY}/userinfo-#{TARGET_USERNAME}.xml", 'w'){|ofile|ofile.write(user_info.body)}

	statuses_count = (Crack::XML.parse(user_info)['user']['statuses_count']).to_f
	puts "#{TARGET_USERNAME} as #{statuses_count} status updates\n\n"

	number_of_pages = ([MAX_NUMBER_OF_TWEETS, statuses_count].min/NUMBER_OF_TWEETS_PER_PAGE).ceil
	puts "This script will iterate through #{number_of_pages} pages"

	File.open("#{DATA_DIRECTORY}/tweets-#{TARGET_USERNAME}.xml", 'w') { |outputfile_user_tweets|(1..number_of_pages).each do |page_number|
		tweets_page = RestClient.get("#{GET_STATUSES_URL}&page=#{page_number}")
		puts "\t Fetching page #{page_number}"
	
		if tweets_page.code == 200
			outputfile_user_tweets.write(tweets_page.body)
			puts "\t\tSuccess!"
		else
			puts "\t\tFailed. Response code: #{tweets_page.code}"
		end
		sleep 2
	end
	}
end


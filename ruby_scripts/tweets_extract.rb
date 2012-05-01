require 'rubygems'

TARGET_USERNAME = "bhogleharsha"
DATA_DIRECTORY = "data-hold"
x = File.new("data-hold/tweets-#{TARGET_USERNAME}.xml", "r").read
fil = "#{DATA_DIRECTORY}/tweet-texts-#{TARGET_USERNAME}.txt"

File.open fil, 'w' do |f|
	f.puts x.scan(/<text>(.*)<\/text>/)
end

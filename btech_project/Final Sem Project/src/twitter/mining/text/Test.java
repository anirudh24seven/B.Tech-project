package twitter.mining.text;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

import twitter4j.Paging;
import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Tweet;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;

public class Test {
    private final static String CONSUMER_KEY = "vmQG1QCDh1iMizdJ3QgdfA";
    private final static String CONSUMER_KEY_SECRET = "nuVrcvR2tRIAVKeNF88nxhGK8FSzaBgeaekoGCYJQU";

    FileWriter fstream;
    BufferedWriter out;
    List<String> tweets = new ArrayList<String>();

	private final Logger logger = Logger.getLogger(Test.class.getName());

    public static void main(String[] args) throws IOException {
        new Test().retrieve();
    }

    public void retrieve() throws IOException {
        logger.info("Retrieving tweets...");
        Twitter twitter = new TwitterFactory().getInstance();
        String user = "cricketaakash";
        Query query = new Query("from:"+user);
        query.setRpp(100);
        
        
		try {
			fstream = new FileWriter("out.txt");			
			out = new BufferedWriter(fstream);
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
        
        
        try {
            QueryResult result = twitter.search(query);
            System.out.println("Count : " + result.getTweets().size()) ;
            for (Tweet tweet : result.getTweets()) {
                //System.out.println("text : " + tweet.getText());
                tweets.add(tweet.getText());
            }
        } catch (TwitterException e) {
            e.printStackTrace();
        }
        
        for(String text:tweets) {
        	System.out.println(text);
        	try {
				out.write(text);
				out.write("\n");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
        
        out.close();
        tokenize();
        System.out.println("done! ");
    }
    
    
    public void tokenize() {
    	
    }
}

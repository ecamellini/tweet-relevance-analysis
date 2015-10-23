# Problems that I encountered

- To check the coordinates from Schipol I created a script that extracts the coordinates from every tweet and checks if they are in the schipol bounding box. The problem was that the 'coordinates' field has value None for the majority of the tweets, because the location filtering is based also on the intersection with predefined places (as stated here https://dev.twitter.com/streaming/overview/request-parameters in the locations section), so I also decided to run again the 2 hours stream sampling using the schipol bounding box, to see the difference.

- To build the script that checks the coordinates I had some problems importing the tweets file as a Pandas dataframe because of newlines introduced by the Python script that reads the stream and because pandas needs a format of the type [{json1},{json2}...], so I needed to do some pre-processing.

- The coordinates in the tweet are in the format {'coordinates': [long, lat], 'type': 'Point'}, but for some reasons I had problems in reading them as jsons with Pandas or the json module, so I decided to parse them by myself.

- For the plots of the mean w.r.t. to the relevance I wanted to plot only the two mean values for the two relevances (0 and 1) in an histogram style, but I wasn't able to do it (the histogram plotted strange data, maybe it can only used for distributions?), so I used the linear plots that you  can find in the paper, even if the x-axis is not continuous but discrete.

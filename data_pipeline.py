from functions import *
import time 
import datetime

print("Starting data pipeline at: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("_____________________________________________________________")

#Step 1: extract video IDs from the YouTube API
t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Step 1: Done")
print("Step 1: Extracting video IDs took: ", str(t1-t0), " seconds", "\n")

#Step 2: extract transcripts for videos
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("Step 2: Done")
print("Step 2: Extracting transcripts took: ", str(t1-t0), " seconds", "\n")

#Step 3: Transform data 
t0 = time.time()
transformData()
t1 = time.time()
print("Step 3: Done")
print("Step 3: Transforming data took: ", str(t1-t0), " seconds", "\n")

#Step 4: Generate text embeddings
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("Step 4: Done")
print("Step 4: Generating embeddings took: ", str(t1-t0), " seconds", "\n")



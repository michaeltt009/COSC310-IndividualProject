#place standford core nlp folder next to this directory and rename the folder to standfordcorenlp
#run this file first to run the server
import os
os.system('cd ..\stanfordcorenlp && java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000')

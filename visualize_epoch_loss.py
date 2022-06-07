import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help="path of the csv file")
args = parser.parse_args()
  
x = []
train_y = []
train_loss = []
test_y = []
test_loss = []
currEpoch = -1
currTrain = -1 # current training average accuracy
currTest = -1 # current testing average accuracy
PreviousIsTest = False

with open(args.file, 'r') as fp:
    for line in fp:
        sentence = line.strip()
        keepSentence = False
        isEpoch = False

        if sentence.find('Epoch') != -1 or sentence.find('Test') != -1:
            keepSentence = True
            if sentence.find('Epoch') != -1:
                isEpoch = True

        if keepSentence:
            if isEpoch: # Training time!
                # save data of test accuracy
                if PreviousIsTest:
                    test_loss.append(currTestLoss)
                    PreviousIsTest = False

                # Get epoch and training accuracy
                currEpoch = int(sentence[sentence.find('[')+1 : sentence.find(']')])
                sentence = sentence[sentence.find('Loss'):] # trim
                currTrainLoss = float(sentence[sentence.find('(')+1 : sentence.find(')')])
                #print("current train loss:", currTrainLoss )
            else: # Test time!
                # save data of epoch and training loss
                if not PreviousIsTest:
                    x.append(currEpoch)
                    #train_y.append(currTrain)
                    train_loss.append(currTrainLoss)
                PreviousIsTest = True
                # get test loss
                sentence = sentence[sentence.find('Loss'):] # trim
                currTestLoss = currTrainLoss = float(sentence[sentence.find('(')+1 : sentence.find(')')])
                #print("current test loss:", currTestLoss ) 
                
    test_loss.append(currTestLoss)
    
# 2. Plot a testing / training loss graph 
# plotting the training points 
plt.plot(x, train_loss, label = "Training loss")
# plotting the testing points 
plt.plot(x, test_loss, label = "Testing loss")  
# naming the x axis
plt.xlabel('Epochs')
# naming the y axis
plt.ylabel('Loss')
# Set the boundary of y axis
#plt.ylim(0, 100)
# giving a title to the graph
plt.title('Training and Testing Loss')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

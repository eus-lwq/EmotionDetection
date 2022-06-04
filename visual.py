import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help="path of the csv file")
args = parser.parse_args()
  
x = []
train_y = []
test_y = []
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
                    test_y.append(currTest)
                    PreviousIsTest = False

                # Get epoch and training accuracy
                currEpoch = int(sentence[sentence.find('[')+1 : sentence.find(']')])
                sentence = sentence[sentence.find('Acc@1'):] # trim
                currTrain = float(sentence[sentence.find('(')+1 : sentence.find(')')])
            else: # Test time!
                # save data of epoch and training accuracy
                if not PreviousIsTest:
                    x.append(currEpoch)
                    train_y.append(currTrain)

                PreviousIsTest = True

                # get test accuracy
                sentence = sentence[sentence.find('Acc@1'):] # trim
                currTest = float(sentence[sentence.find('(')+1 : sentence.find(')')])

    test_y.append(currTest) # save the final test accuracy

# print(x)
# print(train_y)
# print(test_y)

# Plot Graph
# plotting the training points 
plt.plot(x, train_y, label = "Training accuracy")
  
# plotting the testing points 
plt.plot(x, test_y, label = "Testing accuracy")
  
# naming the x axis
plt.xlabel('Epochs')
# naming the y axis
plt.ylabel('Accuracy')
# Set the boundary of y axis
plt.ylim(0, 100)
# giving a title to the graph
plt.title('Training and Testing Accuracy')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
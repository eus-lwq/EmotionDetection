import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help="path of the csv file")
parser.add_argument('-t', '--type', default='acc', type=str, help="y-axis of the plot")
parser.add_argument('-s', '--show', dest='show', action='store_true', help="plot show()")
args = parser.parse_args()
  
x = []
train_y = []
test_y = []
currEpoch = -1
currTrain = -1 # current training average expected variable like accuracy, loss, etc.
currTest = -1 # current testing average expected variable like accuracy, loss, etc.
PreviousIsTest = False

# print(args.type)
if args.type != 'acc' and args.type!= 'loss': # choose the y-axis be accuracy or loss
    args.type = 'acc'
# print(args.type)

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
                # save data of test variable
                if PreviousIsTest:
                    test_y.append(currTest)
                    PreviousIsTest = False

                # Get epoch and training variable
                currEpoch = int(sentence[sentence.find('[')+1 : sentence.find(']')])
                if args.type == 'acc':
                    sentence = sentence[sentence.find('Acc@1'):] # trim
                    currTrain = float(sentence[sentence.find('(')+1 : sentence.find(')')])
                elif args.type == 'loss':
                    sentence = sentence[sentence.find('Loss'):] # trim
                    currTrain = float(sentence[sentence.find('(')+1 : sentence.find(')')])
            else: # Test time!
                # save data of epoch and training variable
                if not PreviousIsTest:
                    x.append(currEpoch)
                    train_y.append(currTrain)

                PreviousIsTest = True

                # get test variable
                if args.type == 'acc':
                    sentence = sentence[sentence.find('Acc@1'):] # trim
                    currTest = float(sentence[sentence.find('(')+1 : sentence.find(')')])
                elif args.type == 'loss':
                    sentence = sentence[sentence.find('Loss'):] # trim
                    currTest = float(sentence[sentence.find('(')+1 : sentence.find(')')])

    test_y.append(currTest) # save the final test variable

# print(x)
# print(train_y)
# print(test_y)

name = str(args.file)
name = name[:-4]

# Plot Graph
if args.type == 'acc':
    # plotting the training points 
    plt.plot(x, train_y, label = "Training accuracy")
    # plotting the testing points 
    plt.plot(x, test_y, label = "Testing accuracy")
    # naming the y axis
    plt.ylabel('Accuracy')
    # Set the boundary of y axis
    plt.ylim(0, 100)
    # giving a title to the graph
    plt.title('Training and Testing Accuracy' + ' (' + name + ')')

elif args.type == 'loss':
    # plotting the training points 
    plt.plot(x, train_y, label = "Training loss")
    # plotting the testing points 
    plt.plot(x, test_y, label = "Testing loss")
    # naming the y axis
    plt.ylabel('Loss')
    # giving a title to the graph
    plt.title('Training and Testing Loss' + ' (' + name + ')')

# naming the x axis
plt.xlabel('Epochs')

# show a legend on the plot
plt.legend()

# save plot as png file
# Generally, pngs are better than jpeg for high-resolution plots as 
# png is a lossless compression format and the other being lossy compression format.
name = name + '_' + args.type + ".png"
plt.savefig(name,dpi=300)

# function to show the plot
if args.show:
    plt.show()


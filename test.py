from Utils.parser import *

parser = parse_args()

print(parser.epoch)

str = parser.weights_path + parser.dataset + '.pth'
print(str)

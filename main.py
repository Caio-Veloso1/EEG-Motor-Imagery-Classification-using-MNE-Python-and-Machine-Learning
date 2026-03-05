from src.preprocess import preprocess_raw
from src.create_epoch import create_epochs
from src.feature_extraction import extract_features
from src.train_model import train

subject = 1 
runs = [6, 10 , 14] 

#cada participante tem 14 runs, porem vou utilizar apenas 3 runs
#run 6 = imaginação do movimento
#run 10 = imaginação
#run 10= imaginação


raw = preprocess_raw(subject, runs)
raw.plot

epoch = create_epochs(raw)

x, y = extract_features(epoch)

model, acc = train(x, y)

print("Accuracy", acc)










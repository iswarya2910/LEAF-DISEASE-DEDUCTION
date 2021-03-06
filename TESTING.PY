Testing code
import os
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from numpy import set_printoptions



# Initial Settings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.chdir(r'C:/Users/admin/Downloads/plantdisease_dataset')
set_printoptions(precision=2, suppress=True)

# Loading Model
my_model = load_model('plant_cnn_0.94.h5')
print(my_model.summary(), '\n')

# Parameters: Weights and Biases
print('Plant CNN last layer bias:')
print(my_model.get_weights()[-1])
print('Plant CNN last layer weights:')
print(my_model.get_weights()[-2])

# Evaluation test\n",
eval_idg = ImageDataGenerator(rescale=1. / 255.)
eval_g = eval_idg.flow_from_directory(directory=r'C:/Users/admin/Downloads/plantdisease_dataset/Testing/',
                                      target_size=(100, 100),
                                      class_mode='binary',
                                      batch_size=125,
                                      shuffle=False)
(eval_loss, eval_acc) = my_model.evaluate_generator(generator=eval_g, steps=1)
print('evaluation Loss over never-before-seen images is: {:.4f}'.format(eval_loss))
print('evaluation Accuracy over never-before-seen images is: {:4.2f}%'.format(eval_acc*100), '\n')

# Individual Predictions
pred_idg = eval_idg
pred_g = eval_g
pred = my_model.predict_generator(generator=pred_g, steps=1)
print(pred_g.filenames, '\n')
print(pred_g.class_indices, '\n')
print(pred[0:5], '\n')

 


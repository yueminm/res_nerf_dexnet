import pickle


with open('Output/grasp.pkl', 'rb') as f:
    data = pickle.load(f)

print('Center: ', data.center)
print('Angle: ', data.angle)
print('Depth: ', data.depth)
print('Distance between jaws [m]: ', data.width)
print('Feature vec: ', data.feature_vec)
print('Contact points: ', data.contact_points)
# print('Grasping Quality: ', data.q_value)
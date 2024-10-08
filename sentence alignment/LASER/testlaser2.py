from laser_encoders import LaserEncoderPipeline
encoder = LaserEncoderPipeline(lang="eng_Latn")
embeddings = encoder.encode_sentences(["Bob isn't hear; he went home","Bob lives on the beach.","Bob has two cats.",
                                       "Bob has a dog.","Bob will be back tomorrow."])
print(embeddings.shape)  # (2, 1024)

print('\n')
print("this is sentence eng")
print('\n')
print(embeddings)
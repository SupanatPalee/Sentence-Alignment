from laser_encoders import LaserEncoderPipeline
encoder = LaserEncoderPipeline(lang="tha_Thai")
# embeddings = encoder.encode_sentences(["บ็อบกลับบ้าน","บ็อบไม่อยู่ที่นี่","บ็อบอาศัยอยู๋บนชายหาด"
#                                        ,"บ็อบมีสุนัขหนึ่งตัวเเละเเมวสองตัว","เเมวของบ็อบชื่อฟลัฟฟี","บ็อบจะกลับมาวันพรุ่งนี้"])
embeddings = encoder.encode_sentences(["ฉันวางเเก้ว","เเก้วไม่อยู๋"])
print(embeddings.shape)  # (2, 1024)

print('\n')
print("this is sentence thai")
print('\n')
print(embeddings)
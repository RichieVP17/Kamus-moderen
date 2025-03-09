meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "LMAO": "Tanggapan untuk sesuatu yang sangat lucu"
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata dari",word,"adalah",meme_dict[word])      
else:
    print("Maap kami tidak dapat menemukan makna",word,"yang dicari")
    

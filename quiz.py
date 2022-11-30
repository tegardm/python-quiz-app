soal_soal = {
    "Siapa presiden pertama indonesia ? " : "A",
    "Ibu kota Indonesia adalah ?" : "A",
    "Kapan tahun Indonesia merdeka ?" : "C",
    "Gaya apa yang mempengaruhi sebuah objek jatuh ke bumi ?":"D",
    "Dibawah ini yang merupakan seorang fisikawan dalam bidang quantum adalah ?":"B"
}

jawaban_jawaban = [['A. Soekarno','B. Soepomo','C. B.J. Habibie','D. Soeharto'],
    ['A. Jakarta','B. Semarang','C. Denpasar','D. Makassar'],
    ['A. 1970','B. 1991','C. 1945','D. 2000'],
    ['A. Gaya Archimedes','B. Gaya Pascal','C. Gaya Sentrifugal','D. Gaya Gravitasi'],
    ['A. Ibnu Sina','B. Richard Feyman','C. Socrates','D. Aristoteles']]


def mulai_game():
    tebakan_jawaban = []
    jawaban_benar = 0
    nomer_soal = 1

    for soal in soal_soal:
        print('-----------------')
        print(soal)
        for jawaban in jawaban_jawaban[nomer_soal-1]:
            print(jawaban)
        tebakan = input("Masukan (A,B,C,D) = ")
        tebakan = tebakan.upper()
        tebakan_jawaban.append(tebakan)
        jawaban_benar += check_jawaban(soal_soal.get(soal),tebakan)
        nomer_soal += 1

    menampilkan_score(jawaban_benar, tebakan_jawaban)


def check_jawaban(jawaban_benar,tebakan_user):
    if (jawaban_benar == tebakan_user):
        print("Jawaban Anda Benar !")
        return 1
    else:
        print("Jawaban Anda Salah !")
        return 0
    
def menampilkan_score(score_benar, jawaban_saya):
    print('-----------------')
    print('HASIL')
    print('-----------------')
    print('Jawaban Saya : ', end='')
    for jawaban in jawaban_saya:
        print(jawaban, end=" ")
    print()

    score = score_benar / len(soal_soal)
    score *= 100
    print('Nilai Kamu : '+ str(int(score))+"%")

def mulai_ulang():
    jawaban = input("Apakah Anda Ingin Mengulang Program ? (yes/no) ")
    jawaban = jawaban.upper()

    if jawaban == 'YES':
        return True
    else:
        return False


mulai_game()

while mulai_ulang():
    mulai_game()
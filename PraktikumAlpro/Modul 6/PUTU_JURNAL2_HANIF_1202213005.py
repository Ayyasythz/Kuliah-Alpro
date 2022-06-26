
with open('KesanPesan.txt', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('==========='):
            lines[i] = lines[i].strip() + '\nUntuk Masukan mungkin terkait dengan asisten ketika sedang menjelaskan ' \
                                          'materi kadang saya melihat hanya ada 1 orang asisten saja yang menjeaskan ' \
                                          'agak kasihan juga soalnya, lalu untuk kesan pesan asisten HOPE dan PUTU ' \
                                          'keduanya udah bagus \n '
    f.seek(0)
    for line in lines:
        f.write(line)


import gradio as gr

demo = gr.Interface(
    fn=prediksi,
    inputs=[
        gr.Number(label="Umur"),
        gr.Number(label="Jenis Kelamin"),
        gr.Number(label="Tipe Dada"),
        gr.Number(label="Tekanan Darah"),
        gr.Number(label="Kolesterol"),
        gr.Number(label="Gula Darah"),
        gr.Number(label="Hasil Rekaman EKG"),
        gr.Number(label="Detak Jantung Maksimum"),
        gr.Number(label="Angina"),
        gr.Number(label="Oldpeak"),
        gr.Number(label="Slope"),
        gr.Number(label="Nilai CA"),
        gr.Number(label="Nilai Thal")
    ],
    outputs="text",
    title="MemPrediksi Penyakit Jantung Menggunakan JST",
    description="""Masukan Data Pasien Kemudian Pencet Summit.AI akan memPrediksi apakah pasien berpotensi terkena penyakit Jantung atau Tidak"""
)

demo.launch()

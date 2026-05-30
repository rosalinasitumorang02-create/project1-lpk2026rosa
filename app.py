import streamlit as st
def hitung_kadar_gravimetri(massa_analit, massa_sampel, faktor_gravimetri=1.0):
    """
    Menghitung % kadar dalam analisis gravimetri.
    
    Parameter:
    massa_analit (float): Massa endapan/analit yang ditimbang (gram).
    massa_sampel (float): Massa sampel awal (gram).
    faktor_gravimetri (float): Faktor gravimetri (Ar/Mr atau Mr_dicari/Mr_ditimbang). Default adalah 1.0.
    
    Rumus:
    % Kadar = (Massa Analit * Faktor Gravimetri) / Massa Sampel * 100%
    """
    if massa_sampel <= 0:
        raise ValueError("Massa sampel harus lebih besar dari nol.")
        
    kadar = (massa_analit * faktor_gravimetri) / massa_sampel * 100
    return kadar

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    print("=== Kalkulator Gravimetri ===")
    try:
        # Contoh: Menghitung kadar Cl dalam sampel (Endapan AgCl)
        # Faktor gravimetri = Ar Cl / Mr AgCl = 35.5 / 143.32 = 0.2477
        m_sampel = float(input("Masukkan massa sampel (g): "))
        m_analit = float(input("Masukkan massa endapan (g): "))
        fg = float(input("Masukkan faktor gravimetri (isi 1 jika tidak ada): ") or 1.0)
        
        hasil = hitung_kadar_gravimetri(m_analit, m_sampel, fg)
        print(f"\nHasil: % Kadar = {hasil:.4f}%")
        
    except ValueError as e:
        print(f"Error: {e}. Pastikan input berupa angka yang valid.")

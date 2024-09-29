import streamlit as st

# Titre de l'application
st.title('Bienvenue sur le Calculateur d\'IMC')

# Prendre le poids en kg
poids = st.number_input("Entrez votre poids (en kilogrammes)")

# Prendre la taille
format_taille = st.radio('Sélectionnez votre format de taille:', ('Centimètres', 'Mètres', 'Pieds'))

if format_taille == 'Centimètres':
    taille = st.number_input('Taille en centimètres')
    try:
        imc = poids / ((taille / 100) ** 2)
    except:
        st.text("Veuillez entrer une taille valide.")
elif format_taille == 'Mètres':
    taille = st.number_input('Taille en mètres')
    try:
        imc = poids / (taille ** 2)
    except:
        st.text("Veuillez entrer une taille valide.")
else:
    taille = st.number_input('Taille en pieds')
    try:
        imc = poids / (((taille / 3.28)) ** 2)
    except:
        st.text("Veuillez entrer une taille valide.")

# Calculer l'IMC et fournir une interprétation
if st.button('Calculer l\'IMC'):
    st.text(f"Votre indice de masse corporelle (IMC) est de {imc:.2f}.")

    # Interprétation de l'IMC avec des recommandations détaillées
    if imc < 16:
        st.error("Vous êtes dans la catégorie 'Dénutrition sévère'.")
        st.text("Interprétation : Cet IMC est très bas et peut indiquer des problèmes de malnutrition ou de santé sous-jacents. "
                "Il est fortement recommandé de consulter un professionnel de santé pour obtenir des conseils sur la prise de poids de manière saine.")
    elif 16 <= imc < 18.5:
        st.warning("Vous êtes dans la catégorie 'Insuffisance pondérale'.")
        st.text("Interprétation : Être en dessous du poids peut suggérer que vous ne recevez pas assez de nutriments. "
                "Envisagez d'améliorer votre alimentation en incluant des aliments plus nutritifs et caloriques, et consultez un professionnel de santé si nécessaire.")
    elif 18.5 <= imc < 25:
        st.success("Vous êtes dans la catégorie 'Poids normal'.")
        st.text("Interprétation : Cet IMC est considéré comme étant dans la fourchette de poids saine pour votre taille. "
                "Maintenez une alimentation équilibrée et une activité physique régulière pour rester en bonne santé.")
    elif 25 <= imc < 30:
        st.warning("Vous êtes dans la catégorie 'Surpoids'.")
        st.text("Interprétation : Le surpoids peut augmenter le risque de développer certaines maladies, comme les maladies cardiaques et le diabète. "
                "Il peut être utile d'évaluer votre alimentation et d'augmenter votre activité physique.")
    else:
        st.error("Vous êtes dans la catégorie 'Obésité'.")
        st.text("Interprétation : Cet IMC indique une obésité, ce qui peut entraîner des risques sérieux pour la santé tels que des maladies cardiovasculaires, "
                "le diabète, et des problèmes articulaires. Il est important d'envisager des changements de mode de vie et de consulter un professionnel de santé pour des conseils personnalisés.")

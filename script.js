document.getElementById("downloadButton").addEventListener("click", function() {
    // Création d'un élément <a> pour le téléchargement
    var downloadLink = document.createElement("a");
    downloadLink.setAttribute("href", "chemin/vers/votre/fichier.zip");
    downloadLink.setAttribute("download", "nom-du-fichier.zip");
    
    // Ajout de l'élément <a> à la page et déclenchement du téléchargement
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  });
  
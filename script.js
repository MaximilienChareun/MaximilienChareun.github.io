document.getElementById("downloadButton").addEventListener("click", function() {
    // Création d'un élément <a> pour le téléchargement
    var downloadLink = document.createElement("a");
    downloadLink.setAttribute("href", "antichoco.zip");
    downloadLink.setAttribute("download", "antichoco.zip");
    
    // Ajout de l'élément <a> à la page et déclenchement du téléchargement
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  });
  
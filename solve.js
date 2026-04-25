Java.perform(function() {
    console.log("[*] Script de hooking chargé.");

    // Nous utilisons Java.choose car la méthode Password() appartient à une instance
    // active de MainActivity qui est déjà présente en mémoire.
    Java.choose("com.pwnsec.firestorm.MainActivity", {
        onMatch: function(instance) {
            console.log("[+] Instance de MainActivity trouvée en mémoire !");
            
            try {
                // Appel manuel de la méthode qui génère le mot de passe
                var result = instance.Password();
                console.log("\n[✨] MOT DE PASSE RÉCUPÉRÉ : " + result + "\n");
            } catch (e) {
                console.log("[-] Erreur lors de l'appel de la méthode : " + e);
            }
        },
        onComplete: function() {
            console.log("[*] Recherche d'instance terminée.");
        }
    });
});
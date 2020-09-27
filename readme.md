# Nicopaleis
## geparametriseerde e-mail template

### Wat is het Nicopaleis?
Het Nicopaleis is een Flask app waar je geparametriseerde e-mail templates kunt aanmaken en beheren. De e-mailberichten bestaan uit een lay-out en een inhoud. Zowel de lay-out als de inhoud kunnen parameters bevatten (`$parameter`). De grondgedachten zijn:

* Scheiding van inhoud en opmaak.
* Geparametriseerde teksten.
* Modulaire opbouw via blokteksten.
* Consistente opmaak van berichten.

### Wat is de use-case?
Je kunt het Nicopaleis gebruiken om berichten een consistente huisstijl mee te geven. De applicatie is bovendien nuttig indien je berichten velden en/of blokteksten bevatten die je op één plek wilt kunnen beheren.

De tool is ontworpen voor de Centrale Studentenadministratie. In hun berichtgeving komen velden voor zoals collegejaar, collegegeldtarieven en url naar het reglement inschrijving die jaarlijks geupdate dienen te worden. Daarnaast bevatten de berichten veel voorkomende blokteksten zoals bezwaarclausules en deadlines. Het is belangrijk dat de berichten opgesteld zijn in de UU-huisstijl en dat de inhoud van de berichten juist is. Deze tool assisteert in dat beheer.

### Versie 2.1
- Preview voor snippets
- Zoeken op `$parameters` en `$snippets`
- Definitie van settings
- Export xml voor inlezen OSIRIS

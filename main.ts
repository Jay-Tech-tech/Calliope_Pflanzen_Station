let Temperatur = 0
let Helligkeit = 0
basic.forever(function () {
    // 1. Sensoren auslesen
    Temperatur = input.temperature()
    Helligkeit = input.lightLevel()
    // 2. Temperatur-Anzeige (RGB-LED)
    if (Temperatur < 28) {
        // Blau
        basic.setLedColor(0x0000ff)
    } else if (Temperatur < 30) {
        // Gelb
        basic.setLedColor(0xffff00)
    } else if (Temperatur < 32) {
        // Rot
        basic.setLedColor(0xff0000)
    }
    // 3. Bodenfeuchtigkeit und Alarm
    if (grove.measureMoistureAnalog(AnalogPin.C16, MoistureMode.Original, MoistureOutput.Number) > 300) {
        basic.showIcon(IconNames.Happy)
        // Schaltet den Dauerton ab, sobald die Pflanze genug Wasser hat
        music.stopAllSounds()
    } else {
        basic.showIcon(IconNames.Sad)
        music.ringTone(131)
    }
    basic.pause(200)
    // 4. Helligkeit (Balkendiagramm)
    if (Helligkeit < 51) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
    } else if (Helligkeit < 102) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
    } else if (Helligkeit < 153) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (Helligkeit < 204) {
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (Helligkeit < 255) {
        // Dieser Block fängt nun automatisch alle verbleibenden
        // Werte ab 204 bis zum physikalischen Maximum von 255 ab.
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    // 5. Wartezeit vor der nächsten Messung
    basic.pause(2000)
})

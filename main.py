Temperatur = 0
Helligkeit = 0

def on_button_b():
    music.stop_all_sounds()
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_forever():
    global Temperatur, Helligkeit
    # 1. Sensoren auslesen
    Temperatur = input.temperature()
    Helligkeit = input.light_level()
    # 2. Temperatur-Anzeige (RGB-LED)
    if Temperatur < 28:
        # Blau
        basic.set_led_color(0x0000ff)
    elif Temperatur < 30:
        # Gelb
        basic.set_led_color(0x00ff00)
    elif Temperatur < 35:
        # Rot
        basic.set_led_color(0xff0000)
    # 3. Bodenfeuchtigkeit und Alarm
    if grove.measure_moisture_analog(AnalogPin.C16, MoistureMode.ORIGINAL, MoistureOutput.NUMBER) > 100:
        basic.show_number(grove.measure_moisture_analog(AnalogPin.C16, MoistureMode.ORIGINAL, MoistureOutput.NUMBER))
        # Schaltet den Dauerton ab, sobald die Pflanze genug Wasser hat
        music.stop_all_sounds()
    else:
        basic.show_icon(IconNames.SAD)
        music.ring_tone(131)
    basic.pause(200)
    # 4. Helligkeit (Balkendiagramm)
    if Helligkeit < 51:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
    elif Helligkeit < 102:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
    elif Helligkeit < 153:
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
    elif Helligkeit < 204:
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    elif Helligkeit < 255:
        # Dieser Block fängt nun automatisch alle verbleibenden
        # Werte ab 204 bis zum physikalischen Maximum von 255 ab.
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    # 5. Wartezeit vor der nächsten Messung
    basic.pause(200)
basic.forever(on_forever)

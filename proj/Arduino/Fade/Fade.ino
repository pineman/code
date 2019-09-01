#include <math.h>

#define RED 9
#define GREEN 11
#define BLUE 10

/*
 * Remember we are pulling pins to ground, so
 * 0% duty cycle = maximum intensity and
 * 100% duty cycle = minimum intensity.
 */

// Maximum intensities (green and blue are too strong compared to red)
#define RED_MAX 0
#define GREEN_MAX 155
#define BLUE_MAX 30

enum MODE {
	RAINBOW,
	SINGLE, // Store one color
	BLINK, // Store two colors and a delay
	FADE // Store two colors and a delay
};

/* Save mode to eeprom when its switched (by button or by software) and
 * some time has past. Use a "saved" flag to know if the mode has been saved.
 * Use update.
 * Everytime mode is switched, set flag DIRTY. Busy loop check serial and if
 * 5 minutes have passed and DIRTY is true, save mode.
 */

// Specify which addresses save what, byte per byte.
enum EEPROM_ADDRESS {
	MODE,
	SINGLE_R,
	SINGLE_G,
	SINGLE_B,
	BLINK_1R,
	BLINK_1G,
	BLINK_1B,
	BLINK_2R,
	BLINK_2G,
	BLINK_2B,
	BLINK_DELAY,
	FADE_1R,
	FADE_1G,
	FADE_1B,
	FADE_2R,
	FADE_2G,
	FADE_2B,
	FADE_DELAY
};

void setcolor(int r, int g, int b)
{
	analogWrite(RED, r);
	analogWrite(GREEN, g);
	analogWrite(BLUE, b);
}

void setup()
{
	pinMode(RED, OUTPUT);
	pinMode(GREEN, OUTPUT);
	pinMode(BLUE, OUTPUT);

	Serial.begin(115200);

	setcolor(255, 255, 255); // Turn off LEDs.
}

void save_config()
{
}

// TODO: needs to be non-blocking
// possible: save what color and direction we are. return the time to wait
// before calling again.
// static int i;
// for (; i ... ; i..) { analogWrite(...); return time_b4_next_iter}
// save which for we're in and then switch based on that to find the for.
/* Start on red and cycle through the color wheel. */
void rainbow(int color_time)
{
	// Start on red
	// Increase blue (to magenta)
	setcolor(0, 255, 255);
	for (int i = 255; i >= 255-191; i--) {
		analogWrite(BLUE, (int) round(((191-255)/191.0)*(255-i)+255));
		delay(color_time);
	}
	for (int i = 255-191-1; i >= BLUE_MAX; i--) {
		analogWrite(BLUE, (int) round((191.0/(191-255))*(255-i)-255*191.0/(191-255)));
		delay(color_time);
	}

	// Decrease red (to blue)
	for (int i = RED_MAX; i <= 255; i++) {
		analogWrite(RED, i);
		delay(color_time);
	}

	// Increase green (to cyan)
	for (int i = 255; i >= GREEN_MAX; i--) {
		analogWrite(GREEN, i);
		delay(color_time);
	}

	// Decrease blue (to green)
	for (int i = BLUE_MAX; i <= 255; i++) {
		analogWrite(BLUE, i);
		delay(color_time);
	}

	// Increase red (to yellow)
	for (int i = 255; i >= RED_MAX; i--) {
		analogWrite(RED, i);
		delay(color_time);
	}

	// Decrease green (to red)
	// Stretch the time instead of messing about with functions.
	for (int i = GREEN_MAX; i <= 230; i++) {
		analogWrite(GREEN, i);
		delay(color_time/1.5);
	}
	for (int i = 230; i <= 255; i++) {
		analogWrite(GREEN, i);
		delay(color_time*6);
	}
	for (int i = 0; i <= GREEN_MAX-50; i++) {
		delay(color_time);
	}
}

void loop()
{
	rainbow(10);
}

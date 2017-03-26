#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <curses.h>

#define WIDTH 60
#define HEIGHT 20
// Cursor modes
#define INV 0
#define NOR 1
#define VVIS 2 // blink on urxvt

#define QUIT -1

char *choices[] = {
	"Join the loominatey",
	"I never asked for this.",
	"???",
	"WARNING: Do not press.",
	"Quit"
};

int n_choices = sizeof(choices) / sizeof(char *);

void update_stdscr(WINDOW *stdscr);
WINDOW *init_menu(void);
void update_menu(WINDOW *menu_win, int highlight);

int main()
{
	int highlight = 1;
	int choice = 0;
	int c = 0;

	// init our stdscr
	WINDOW *stdscr = initscr();
	noecho();
	curs_set(INV);
	cbreak();
	nonl();

	// initial stdscr update
	update_stdscr(stdscr);

	// init our menu
	WINDOW *menu = init_menu();

	// initial menu update
	update_menu(menu, highlight);

	// Draw
	doupdate();

	while (1) {
		c = wgetch(menu);

		switch (c) {
			case KEY_UP:
				if (highlight == 1)
					highlight = n_choices;
				else
					highlight--;
				update_menu(menu, highlight);
				break;

			case KEY_DOWN:
				if (highlight == n_choices)
					highlight = 1;
				else
					highlight++;
				update_menu(menu, highlight);
				break;

			case KEY_RESIZE:
				erase();
				update_stdscr(stdscr);
				delwin(menu);
				menu = init_menu();
				update_menu(menu, highlight);
				break;

			case 'q':
				choice = QUIT;
				break;

			case '\r': // return key (aka enter)
				choice = highlight;
				/* TODO: The best way to handle this string is
				* probably to create a new window and erase it when needed */
				move(4, 1);
				clrtoeol();
				mvaddch(4, COLS-1, ACS_VLINE); // restore the frame we destroyed
				mvprintw(4, 1, "Enter key was pressed.");
				wnoutrefresh(stdscr); // flush changes
				break;

			default:
				/* TODO: The best way to handle this string is
				* probably to create a new window and erase it when needed */
				move(4, 1);
				clrtoeol();
				mvaddch(4, COLS-1, ACS_VLINE); // restore the frame we destroyed
				mvprintw(4, 1, "Character pressed was '%c' (%03d ASCII.)", c, c);
				wnoutrefresh(stdscr); // flush changes
				break;
		}

		if (choice) {
			/* User chose, come out of the infinite loop */
			break;
		}

		doupdate(); // Render changes
	}

	if (choice != QUIT) {
		mvprintw(6, 1, "You chose: \"%s\"", choices[choice - 1]);
		refresh();
		sleep(2);
	}

	delwin(menu);
	delwin(stdscr);
	endwin();

	return 0;
}

void update_stdscr(WINDOW *stdscr)
{
	box(stdscr, 0, 0);
	mvprintw(1, 1, "Use the arrow keys to move.");
	mvprintw(2, 1, "Press <return> to select.");
	mvprintw(3, 1, "Press <q> to quit.");

	wnoutrefresh(stdscr); // flush changes
}

WINDOW *init_menu(void)
{
	// I think this is pretty smart
	int lines, cols;
	getmaxyx(stdscr, lines, cols);

	int startx = (cols - WIDTH) / 2;
	int starty = (lines - HEIGHT) / 2;

	WINDOW *menu = newwin(HEIGHT, WIDTH, starty, startx);
	keypad(menu, TRUE);
	box(menu, 0, 0);

	return menu;
}

void update_menu(WINDOW *menu, int highlight)
{
	int x = 2;
	int y = 2;

	for (int i = 0; i < n_choices; i++, y++) {
		if (highlight == i + 1) {
			/* Highlight the present choice */
			wattron(menu, A_REVERSE);
			mvwprintw(menu, y, x, "%s", choices[i]);
			wattroff(menu, A_REVERSE);
		}
		else {
			mvwprintw(menu, y, x, "%s", choices[i]);
		}
	}

	wnoutrefresh(menu); // flush changes
}

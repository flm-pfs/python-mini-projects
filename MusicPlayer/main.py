import pygame


class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False

    def load_music(self, file_path):
        pygame.mixer.music.load(file_path)

    def play_music(self):
        pygame.mixer.music.play()
        self.playing = True

    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def unpause_music(self):
        if not self.playing:
            pygame.mixer.music.unpause()
            self.playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False


def main():
    player = MusicPlayer()
    # Replace with your music file path
    file_path = r"MusicPlayer\flmjobsviralshorts.mp3"
    player.load_music(file_path)

    while True:
        print("1. Play Music")
        print("2. Pause Music")
        print("3. Unpause Music")
        print("4. Stop Music")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player.play_music()
        elif choice == '2':
            player.pause_music()
        elif choice == '3':
            player.unpause_music()
        elif choice == '4':
            player.stop_music()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

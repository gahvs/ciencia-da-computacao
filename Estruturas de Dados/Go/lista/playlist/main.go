package main

import "fmt"

func main() {

	fmt.Printf("Main is here\n\n\n")

	myPlaylist := criarPlaylist("Thrash Metal")

	// myPlaylist.adcionarMusica("Master of Puppets", "Metallica", "Master Of Puppets")
	// myPlaylist.adcionarMusica("Peace Sells... But Who's Buying?", "Megadeth", "Peace Sells... But Who's Buying?")
	// myPlaylist.adcionarMusica("Season In the Abyss", "Slayer", "Season in The Abyss")
	// myPlaylist.adcionarMusica("The Four Horsemen", "Metallica", "Kill 'em All")
	// myPlaylist.adcionarMusica("Holy Wars... The Punishment Due", "Megadeth", "Rust in Peace")

	myPlaylist.mostrarMusicasDaPlaylist()

}

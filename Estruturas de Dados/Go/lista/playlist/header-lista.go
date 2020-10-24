package main

import "fmt"

type musica struct {
	nome    string
	artista string
	album   string
	proxima *musica
}

type playlist struct {
	nome    string
	head    *musica
	tocando *musica
}

func criarPlaylist(nome string) *playlist {
	return &playlist{
		nome: nome,
	}
}

func (ctxPlaylist *playlist) adcionarMusica(nome, artista, album string) error {
	musica := &musica{
		nome:    nome,
		artista: artista,
		album:   album,
	}

	if ctxPlaylist.head == nil {
		//Playlist vazia
		ctxPlaylist.head = musica
	} else {
		//Playlist preenchida
		noAtual := ctxPlaylist.head
		for noAtual.proxima != nil {
			//Percorre a Playlist até o "final"
			noAtual = noAtual.proxima
		}
		//Adiciona a música no "fim" da Playlist
		noAtual.proxima = musica
	}
	return nil
}

func (ctxPlaylist *playlist) mostrarMusicasDaPlaylist() error {
	noAtual := ctxPlaylist.head
	if noAtual == nil {
		fmt.Printf("Não há músicas na Playlist %s.", ctxPlaylist.nome)
		return nil
	}

	fmt.Printf("%+v\n", *noAtual)
	for noAtual.proxima != nil {
		noAtual = noAtual.proxima
		fmt.Printf("%+v\n", *noAtual)
	}
	return nil
}

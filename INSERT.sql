INSERT INTO artist(id, name)
    VALUES (1, 'artist_1'),
     (2, 'artist_2'),
     (3, 'artist_3'),
     (4, 'artist_4'),
     (5, 'artist_5'),
     (6, 'artist_6'),
     (7, 'artist_7'),
     (8, 'artist_8');
    
INSERT INTO genre(id, name)
    VALUES(1, 'genre_1'),
    (2, 'genre_2'),
    (3, 'genre_3'),
    (4, 'genre_4'),
    (5, 'genre_5');
    
INSERT INTO album(id, name, releasedate)
    VALUES(1, 'album_1', '1990-12-14'),
    (2, 'album_2', '2010-11-13'),
    (3, 'album_3', '2020-10-20'),
    (4, 'album_4', '1992-9-11'),
    (5, 'album_5', '2000-7-14'),
    (6, 'album_6', '2019-2-27'),
    (7, 'album_7', '2021-1-4'),
    (8, 'album_8', '2005-3-4'),
    (9, 'album_9', '2018-1-20'),
    (10, 'album_10', '2018-10-12');

INSERT INTO track(id, name, tracklength)
    VALUES(1, 'track_1', 3.20),
    (2, 'track_2', 4.30),
    (3, 'track_3', 2.10),
    (4, 'track_4', 2.15),
    (5, 'track_5', 3.12),
    (6, 'track_6', 4.12),
    (7, 'track_7', 3.01),
    (8, 'track_8', 2.25),
    (9, 'track_9', 3.04),
    (10, 'track_10', 2.17),
    (11, 'track_11', 4.40),
    (12, 'track_12', 2.00),
    (13, 'track_13', 3.19),
    (14, 'track_14', 3.27),
    (15, 'track_15', 4.45),
    (16, 'track_16', 1.17);
    (17, 'my_track_best', '4.20'),
    (18, 'my_test_my', '3.50');
    
INSERT INTO collections(id, name, release_year)
    VALUES(1, 'collection_1', '1992-11-13'),
    (2, 'collection_2', '2014-12-23'),
    (3, 'collection_3', '2000-9-22'),
    (4, 'collection_4', '1995-10-21'),
    (5, 'collection_5', '2001-8-15'),
    (6, 'collection_6', '2020-12-27'),
    (7, 'collection_7', '2007-11-14'),
    (8, 'collection_8', '2003-10-21');
    
INSERT INTO album_artist(id, artist_id, album_id)
    VALUES(1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 7, 7),
    (8, 8, 8);
    
INSERT INTO collections_album_track(id, collections_id, album_id, track_id)
    VALUES(1, 1, 1, 1),
    (2, 2, 2, 2),
    (3, 3, 3, 3),
    (4, 4, 4, 4),
    (5, 5, 5, 5),
    (6, 6, 6, 6),
    (7, 7, 7, 7),
    (8, 8, 8, 8);
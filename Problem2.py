# Problem 2 : Favourite Genres
# Time Complexity : O(m*n) where m is the number of users and n is the number of the songs
# Space Complexity : O(m*n) where m is the number of users and n is the number of the songs
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

from collections import defaultdict

def favorite_genre(user_map, genre_map):
    # define hashmap for the result
    result = {}
    # define hashmap songToGenre which will store song as key and genre as value
    songToGenre = {}
    
    # loop though the genre_map hash map
    for genre, songs in genre_map.items():
        # loop through songs list for the genre
        for song in songs:
            # add the genre value for the song key in the songToGenre hashmap
            songToGenre[song] = genre
    # loop through user_map hash map
    for user, songs in user_map.items():
        # define countMap dictionary with default as int
        countMap = defaultdict(int)
        # define maxCount variable and set to 0
        maxCount = 0
        # loop theough songs list
        for song in songs:
            # get the genre for that song from songToGenre hash map
            genre = songToGenre.get(song)
            # check if the genre is not none
            if genre:
                # increment the value for the genre key in the countMap hash map
                countMap[genre] += 1
                # get the maximum between maxCount and value of the genre key in the countMap hash map
                maxCount = max(maxCount,countMap[genre])
        # loop through the countMap hash map
        for genre, count in countMap.items():
            # check if the count for the genre in the countMap is equal to maxCount
            if count == maxCount:
                # if it is then add the genre to user key in the result hash map
                result[user] = genre
    # return result hash map
    return result

    
# Example usage
user_songs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}

song_genres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}

res = favorite_genre(user_songs, song_genres)
print(res)
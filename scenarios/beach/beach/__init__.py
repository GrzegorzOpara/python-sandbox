def checkSpace(beach, spots):
    longest_consequitve_free_spots = 0
    consequitve_free_spots = 0
    for spot in beach:
        if spot == 'T':
            longest_consequitve_free_spots = consequitve_free_spots
            consequitve_free_spots = 0
        else:
            consequitve_free_spots += 1

        if longest_consequitve_free_spots >= spots:
            return True
        
    return False


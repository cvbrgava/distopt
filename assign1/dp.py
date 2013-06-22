def dynamicprog( weights , values, volume ):
	for index in range( len( weights ) ) :
		if index == 0 :
			old = [ (0,[0]) if weights[index] > vol else (values[index], [1]) for vol in range( volume + 1 )]
                	new = old 
		else :
			old = new
        		new = [ (old[vol][0], old[vol][1]+[0])  for vol in range( volume + 1 ) if vol < weights[ index ]]+[ (old[vol][0], old[vol][1]+ [0]) if (old[vol][0]) > (values[ index ] + old[vol - weights[ index ] ][0])  else (values[ index ] + old[vol - weights[ index ] ][0], old[vol - weights[ index ] ][1]+[1])  for vol in range( volume + 1 ) if vol >= weights[ index ] ]
        return new[ -1 ][ 0 ] , new[ -1 ] [ 1 ] 



if __name__=="__main__":
	values = [16,19,23,28]
	weights = [2,3,4,5] 
	volume = 7
	value_opt, choice_opt = dynamicprog( weights , values, volume )
	print value_opt, choice_opt





	

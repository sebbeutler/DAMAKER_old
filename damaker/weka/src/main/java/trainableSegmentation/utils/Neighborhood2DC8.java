/*-
 * #%L
 * Fiji distribution of ImageJ for the life sciences.
 * %%
 * Copyright (C) 2010 - 2022 Fiji developers.
 * %%
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public
 * License along with this program.  If not, see
 * <http://www.gnu.org/licenses/gpl-3.0.html>.
 * #L%
 */
package trainableSegmentation.utils;

import java.util.ArrayList;

public class Neighborhood2DC8 extends Neighborhood2D {

	private ArrayList<Cursor2D> neighbors = new ArrayList<Cursor2D>();
	
	@Override
	public Iterable<Cursor2D> getNeighbors() 
	{
		neighbors.clear();
		
		final int x = super.cursor.getX();
		final int y = super.cursor.getY();
		
		neighbors.add( new Cursor2D( x-1, y-1 ) );
		neighbors.add( new Cursor2D( x-1, y   ) );
		neighbors.add( new Cursor2D( x-1, y+1 ) );
		neighbors.add( new Cursor2D(   x, y-1 ) );
		neighbors.add( new Cursor2D(   x, y+1 ) );
		neighbors.add( new Cursor2D( x+1, y-1 ) );
		neighbors.add( new Cursor2D( x+1, y   ) );
		neighbors.add( new Cursor2D( x+1, y+1 ) );
		
		return neighbors;
	}

}

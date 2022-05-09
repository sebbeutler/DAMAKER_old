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

import java.util.concurrent.atomic.AtomicLong;

/**
*
* License: GPL
*
* This program is free software; you can redistribute it and/or
* modify it under the terms of the GNU General Public License 2
* as published by the Free Software Foundation.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
*
* Author: Ignacio Arganda-Carreras
*/

/**
* Class to store integer pixel coordinates and its 
* corresponding double value 
* 
* @author Ignacio Arganda-Carreras
*/

public class PixelRecord implements Comparable<PixelRecord>{

	private Cursor2D cursor = null;
	private double value = 0;
	private final static AtomicLong seq = new AtomicLong();
	private final long seqNum;
	
	public PixelRecord(
			final Cursor2D cursor,
			final double value)
	{
		this.cursor = cursor;
		this.value = value;
		seqNum = seq.getAndIncrement();
	}
	
	public PixelRecord(
			final int x,
			final int y,
			final double value )
	{
		this.cursor = new Cursor2D( x, y );
		this.value = value;
		seqNum = seq.getAndIncrement();
	}
	
	
	public Cursor2D getCursor()
	{
		return cursor;
	}
	
	public double getValue()
	{
		return value;
	}

	/**
	 * Compare with a pixel record based on its value and
	 * timestamp
	 * @param v2 voxel record to compare with
	 * @return a value smaller than 0 if the v2 voxel value is 
	 * 			larger this record voxel value, a value larger
	 * 			than 0 if it is lower. If equal, the records
	 * 			created before are set as smaller.  
	 */
	@Override
	public int compareTo( PixelRecord v2 ) 
	{
		int res = Double.compare( value, v2.value );
		if( res == 0 )
			res = (seqNum < v2.seqNum ? -1 : 1);
		
		return res;
	}

}

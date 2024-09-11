package com.gamemode.tkviewer.file_handlers;

import com.gamemode.tkviewer.Tile;

import java.io.File;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;

public class CmpFileHandler extends FileHandler {

    public int mapWidth;
    public int mapHeight;

    public List<Tile> mapTiles;

    public CmpFileHandler(String filepath) {
        this(new File(filepath));
    }

    public CmpFileHandler(File file) {
        super(file);

        // CMAP
        this.seek(4, true);

        long dimensions = this.readInt(true, true);
        this.mapWidth = (int) dimensions & 0x0000FFFF;
        this.mapHeight = (int) dimensions >> 0x10;

        ByteBuffer data = this.readCompressed(true);

        this.mapTiles = new ArrayList<Tile>();
        for (int i = 0; i < (data.capacity() / 6); i++) {
            int idx = (i * 6);
            int abTile = (data.getShort(idx) & 0xffff) - 1;
            int passableTile = data.getShort(idx + 2);
            int sObjTile = (data.getShort(idx + 4) & 0xffff) - 1;

            this.mapTiles.add(new Tile(abTile, passableTile, sObjTile));
        }

        this.close();
    }

    public int getIndex(int x, int y) {
        if (x < 0 || x >= this.mapWidth || y < 0 || y >= this.mapHeight) {
            return -1;
        }
        return y * this.mapWidth + x;
    }

    public int[] getCoordinates(int index) {
        if (index < 0 || index >= this.mapWidth * this.mapHeight) {
            return null;
        }
        int x = index % this.mapWidth;
        int y = index / this.mapWidth;
        return new int[]{x, y};
    }

    @Override
    public ByteBuffer toByteBuffer() {
        // Not implemented
        return null;
    }
}

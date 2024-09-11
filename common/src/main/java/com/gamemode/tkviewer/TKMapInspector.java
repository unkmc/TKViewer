package com.gamemode.tkviewer;

import com.gamemode.tkviewer.file_handlers.CmpFileHandler;
import com.gamemode.tkviewer.file_handlers.DatFileHandler;
import com.gamemode.tkviewer.render.PartRenderer;
import com.gamemode.tkviewer.resources.Resources;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

/**
 * Dumps Image Frames from TKViewer types
 */
public class TKMapInspector {
  public static void inspectSingleFile(String filePath) {
    CmpFileHandler cmpFileHandler = new CmpFileHandler(filePath);

    boolean missingTile = false;
    for (int i = 0; i < cmpFileHandler.mapTiles.size(); i++) {
      Tile tile = cmpFileHandler.mapTiles.get(i);
      if (tile.getAbTile() == -1 && tile.getPassableTile() == 0 && tile.getSObjTile() == -1) {
        missingTile = true;
        break;
      }
    }
    if (!missingTile) {
      System.out.println(filePath + " seems to be complete.");
    }
  }

  public static void main(String[] args) {
    String mapDirectory = Resources.NTK_MAP_DIRECTORY;

    // String testPath = mapDirectory + "/" + "TK000038.cmp";
    // inspectSingleFile(testPath);

    File dir = new File(mapDirectory);
    File[] files = dir.listFiles((d, name) -> name.endsWith(".cmp"));
    if (files != null) {
      for (File file : files) {
        inspectSingleFile(file.getPath());
      }
    } else {
      System.err.println("No CMP files found in directory: " + mapDirectory);
    }
  }
}

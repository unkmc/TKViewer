package com.gamemode.tkviewer;

import com.gamemode.tkviewer.file_handlers.DatFileHandler;
import com.gamemode.tkviewer.render.PartRenderer;
import com.gamemode.tkviewer.resources.Resources;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * Dumps Image Frames from TKViewer types
 */
public class TKDumper {

    private static final String NTK_FRAMES_OUTPUT_DIR = "E:\\Reversing\\NTK\\frames_ntk";
    private static final String BARAM_FRAMES_OUTPUT_DIR = "E:\\Reversing\\NTK\\frames_baram";
    private static final String NTK_DAT_OUTPUT_DIR = "E:\\Reversing\\NTK\\dat_files_ntk";
    private static final String BARAM_DAT_OUTPUT_DIR = "E:\\Reversing\\NTK\\dat_files_baram";

    private static final String META_NEW = "C:\\Users\\mismatch\\Downloads\\meta\\Meta.dat";
    private static final String META_OLD = "C:\\Users\\mismatch\\Downloads\\meta\\Meta_old.dat";

    public static void main(String[] args) {
        DatFileHandler datFileHandler = new DatFileHandler(META_NEW, false);
        datFileHandler.exportFiles("C:\\Users\\mismatch\\Downloads\\meta\\Meta");
        DatFileHandler datFileHandler_old = new DatFileHandler(META_OLD, false);
        datFileHandler.exportFiles("C:\\Users\\mismatch\\Downloads\\meta\\Meta_old");


//
//        (new File(NTK_FRAMES_OUTPUT_DIR)).mkdirs();
//        (new File(BARAM_FRAMES_OUTPUT_DIR)).mkdirs();
//        (new File(NTK_DAT_OUTPUT_DIR)).mkdirs();
//        (new File(BARAM_DAT_OUTPUT_DIR)).mkdirs();
//
////        extractDats(Resources.NTK_DATA_DIRECTORY, NTK_DAT_OUTPUT_DIR, false);
////        extractDats(Resources.BARAM_DATA_DIRECTORY, BARAM_DAT_OUTPUT_DIR, true);
//
//        System.out.println("===============BEGIN TK RENDERING===========");
//        dumpAllImages("Sword", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Spear", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Body", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Fan", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Shield", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Bow", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Coat", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Face", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Hair", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Mantle", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Shoes", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("efx", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Emotion", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("face", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("hair", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("hairdec", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("head", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("headsp", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("helmet", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("misc", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("mon", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("neck", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("tile", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        dumpAllImages("tilec", Resources.NTK_DATA_DIRECTORY, NTK_FRAMES_OUTPUT_DIR);
//        System.out.println("===============END TK RENDERING===========");
//
//        System.out.println("===============BEGIN BARAM RENDERING===========");
//        dumpAllImages("Body", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Spear", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Sword", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Riding", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Shield", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Fan", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Body", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Body", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Bow", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("BowF", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Coat", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Face", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Fan", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Hair", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("HairB", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Mantle", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("MantleF", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("MantleB", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Shield", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Shoes", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("ShoesB", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("ShoesF", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Spear", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("Sword", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("SwordF", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        dumpAllImages("SwordB", Resources.BARAM_DATA_DIRECTORY, BARAM_FRAMES_OUTPUT_DIR);
//        System.out.println("===============END BARAM RENDERING===========");

    }

    private static void extractDats(String dataDirectory, String dumpDirectory, boolean isBaram) {
        File dataDirectoryFile = new File(dataDirectory);
        System.out.println("Extracting dat: " + dataDirectoryFile.getPath());
        File[] datFiles = dataDirectoryFile.listFiles((dir, name) -> name.contains(".dat"));
        for (File datFile : datFiles) {
            System.out.println("Extracting dat: " + datFile.getPath());
            DatFileHandler datFileHandler = new DatFileHandler(datFile.getPath(), isBaram);
            File datDumpDirectory = new File(dumpDirectory + File.separator + datFile.getName());
            datDumpDirectory.mkdirs();
            datFileHandler.exportFiles(datDumpDirectory.getPath());
        }
    }

    private static void dumpAllFiles(DatFileHandler datFileHandler, String baseDirectoryString) {
        System.out.println("Will export extracted dat to: " + baseDirectoryString);
        File outputDirectory = new File(baseDirectoryString);
        if (!outputDirectory.exists()) {
            outputDirectory.mkdirs();
        }

        datFileHandler.exportFiles(baseDirectoryString);
    }

    private static void dumpAllImages(String type, String dataDirectory,String outputDirectoryString) {
        System.out.println("Dumping images for: " + type);
        try {
            PartRenderer  renderer= new PartRenderer(type, dataDirectory);
            File outputDirectory = new File(outputDirectoryString + File.separator + type);
            if (!outputDirectory.exists() && outputDirectory.mkdirs()) {
                System.err.println("Unable to create output directory: " + outputDirectoryString);
            }

            for (int i = 0; i < renderer.getCount(); i++) {
                Image[] images = renderer.getFrames(i);
                String epfName = renderer.getEpfNameForFrame(i);
                for (int j = 0; j < images.length; j++) {
                    try {
                        File file = new File(
                                outputDirectory + File.separator
                                        + epfName + File.separator
                                        + String.format("%05d", i) + File.separator
                                        + String.format("%05d", j) + ".png");
                        file.getParentFile().mkdirs();
                        file.createNewFile();
                        ImageIO.write((BufferedImage) images[j], "png", file);
                    } catch (IOException ioe) {
                        ioe.printStackTrace();
                    }
                }
            }
        } catch (Exception error) {
            System.out.println("Could not parse files for " + type);
            System.out.println(error);
        }
    }
}
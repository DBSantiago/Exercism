public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        int minutesInOven = 40;
        return minutesInOven;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int minutesCookedInOven) {
        return (expectedMinutesInOven() - minutesCookedInOven);
    }
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int lasagnaLayers){
        int minutesPerLayer = 2;
        return (lasagnaLayers * minutesPerLayer);
    }
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int lasagnaLayers, int minutesCookedInOven){
        return (preparationTimeInMinutes(lasagnaLayers) + minutesCookedInOven);
    }
}

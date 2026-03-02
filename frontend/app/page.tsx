"use client";

import {useState,  useEffect} from "react";

interface Workouts{
  id: number;
  date: string;
  type: string;
  duration: number;
  distance: number
  tss: number;
  notes: string
}


export default function Home() {

  const [workouts, setWorkouts] = useState<Workouts[]>([])

  useEffect(() => {
    fetch('http://localhost:8000/workouts')
      .then(response => response.json())
      .then(obj => setWorkouts(obj))
  }, [])

  console.log(workouts)

  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold text-blue-600">
        My Workout Dashboard
      </h1>
      
      {workouts.map((workout) =>
    
        <div key={workout.id}>
          <p>
            type: {workout.type} <br/>
            duration: {workout.duration} <br/>
            date: {workout.date} <br/>
            distance: {workout.distance} <br/>
          </p>
        </div>
  
      )}


    </main>
  );
}


    
"use client";

import {useState,  useEffect} from "react";


interface Workouts{
  id: Number;
  date: string;
  type: string;
  duration: Number;
  distance: Number
  tss: Number;
  notes: string

}

const [workouts, setWorkouts] = useState<Workouts[]>([])


export default function Home() {
  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold text-blue-600">
        My Workout Dashboard
      </h1>
      <p className="mt-4 text-gray-600">
        Connecting to FastAPI soon...
      </p>
    </main>
  );
}

    // id: Optional[int]  = Field(default=None,primary_key=True)
    // date: date
    // type: str
    // duration: int
    // distance: float
    // tss: Optional[int]
    // notes: Optional[str]
    
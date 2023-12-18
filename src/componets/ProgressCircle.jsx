// import React from 'react';

// function ProgressCircle({ progress }) {
//   const radius = 50;
//   const strokeWidth = 10;
//   const normalizedRadius = radius - strokeWidth / 2;
//   const circumference = normalizedRadius * 2 * Math.PI;

//   // Ensure progress is between 0 and 1
//   const validProgress = Math.min(Math.max(progress, 0), 1);
//   const strokeDashoffset = circumference - validProgress * circumference;

//   return (
//     <svg
//       height={radius * 2}
//       width={radius * 2}
//     >
//       <circle
//         stroke="green"
//         fill="red"
//         strokeWidth={strokeWidth}
//         strokeDasharray={circumference}
//         style={{ strokeDashoffset }}
//         r={normalizedRadius}
//         cx={radius}
//         cy={radius}
//       />
//     </svg>
//   );
// }

// export default ProgressCircle;
import React from 'react';

function ProgressCircle({ progress }) {
  const radius = 50;
  const strokeWidth = 10;
  const normalizedRadius = radius - strokeWidth / 2;
  const circumference = normalizedRadius * 2 * Math.PI;

  // Ensure progress is between 0 and 1
  const validProgress = Math.min(Math.max(progress, 0), 1);
  const strokeDashoffset = circumference - validProgress * circumference;

  return (
    <svg
      height={radius * 2}
      width={radius * 2}
    >
      {/* Red Circle (Background) */}
      <circle
        stroke="red"
        fill="transparent"
        strokeWidth={strokeWidth}
        r={normalizedRadius}
        cx={radius}
        cy={radius}
      />

      {/* Green Circle (Progress) */}
      <circle
        stroke="green"
        fill="transparent"
        strokeWidth={strokeWidth}
        strokeDasharray={circumference}
        style={{ strokeDashoffset }}
        r={normalizedRadius}
        cx={radius}
        cy={radius}
      />
    </svg>
  );
}

export default ProgressCircle;
